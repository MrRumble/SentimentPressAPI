import React, { useState, useEffect, useRef } from "react";
import { Line } from "react-chartjs-2";
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  TimeScale,
} from "chart.js";
import "chartjs-adapter-luxon";
import ChartAnnotation from "chartjs-plugin-annotation";
import { FaExpandArrowsAlt } from "react-icons/fa";
import { TiArrowMinimise } from "react-icons/ti";
import { GrClear } from "react-icons/gr";


import { useRefresh } from "../../pages/RefreshContext";


ChartJS.register(ChartAnnotation, Title, Tooltip, Legend, CategoryScale, LinearScale, PointElement, LineElement, TimeScale);
ChartJS.defaults.plugins.legend.labels.color = "white";
ChartJS.defaults.plugins.tooltip.bodyColor = "white";
ChartJS.defaults.plugins.tooltip.titleColor = "white";

const SentimentChart = ({ searchTerm }) => {
  const [chartData, setChartData] = useState({ datasets: [] });
  const [isFullScreen, setIsFullScreen] = useState(false);
  const chartRef = useRef(null);
  const { refreshKey } = useRefresh();

  useEffect(() => {
    if (!searchTerm) return;
  
    const fetchData = async () => {
      try {
        const baseURL = process.env.REACT_APP_API_BASE_URL;
        const response = await fetch(`${baseURL}/api/get_sentiment?search_term=${searchTerm}`);
        const data = await response.json();
  
        const newDataset = {
          label: searchTerm,
          data: data.datasets[0].data.map((item) => ({
            x: new Date(item.x),
            y: item.y,
            summary: item.summary,
          })),
          borderColor: getRandomColor(),
          fill: false,
          tension: 0.4,
          pointRadius: 4,
        };
  
        setChartData((prevChartData) => {
          const existingDatasetIndex = prevChartData.datasets.findIndex(
            (dataset) => dataset.label === searchTerm
          );
  
          if (existingDatasetIndex !== -1) {
            const updatedDatasets = [...prevChartData.datasets];
            updatedDatasets[existingDatasetIndex] = {
              ...updatedDatasets[existingDatasetIndex],
              data: newDataset.data,
            };
            return { datasets: updatedDatasets };
          } else {
            return {
              datasets: [...prevChartData.datasets, newDataset],
            };
          }
        });
      } catch (error) {
        console.error("Error fetching sentiment data:", error);
      }
    };
  
    fetchData();
  }, [searchTerm, refreshKey]);
  
  

  const clearChart = () => {
    setChartData({ datasets: [{ label: "", data: [], borderColor: "transparent", fill: false }] });
  };
  

  const getRandomColor = () => {
    const letters = "456789ABCDEF";
    let color = "#";
    for (let i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random() * letters.length)];
    }
    return color;
  };

  const options = {
    responsive: true,
    plugins: {
      legend: {
        display: chartData.datasets.length > 0,
      },
      title: {
        display: true,
        text: "Mean Sentiment Over Time",
        color: "white",
      },
      tooltip: {
        backgroundColor: "rgba(0, 0, 0, 0.58)",
        borderColor: "rgb(198, 0, 205)",
        borderWidth: 1,
        cornerRadius: 8,
        displayColors: false,
        position: "nearest",
        caretPadding: 30,
        xAlign: "center",
        yAlign: "bottom",
        callbacks: {
          title: () => "",
          label: (tooltipItem) => {
            const point = tooltipItem.raw;
            const formattedDate = new Intl.DateTimeFormat("en-GB", {
              weekday: "short",
              year: "numeric",
              month: "short",
              day: "numeric",
            }).format(point.x);
      
            const summaryLines = point.summary.match(/.{1,50}(\s|$)/g) || [point.summary];
      
            return [
              `Date: ${formattedDate}`,
              `Sentiment: ${point.y}`,
              `Summary:`,
              ...summaryLines,
            ];
          },
        },
        intersect: false,
        mode: "nearest",
      },
      annotation: {
        annotations: [
          {
            type: "box",
            yMin: 0,
            yMax: 1,
            backgroundColor: "rgba(0,255,0,0.2)",
            borderWidth: 1,
          },
          {
            type: "box",
            yMin: -1,
            yMax: 0,
            backgroundColor: "rgba(255, 0, 0, 0.22)",
            borderWidth: 1,
          },
        ],
      },
    },
    scales: {
      x: {
        type: "time",
        time: {
          unit: "day",
          tooltipFormat: "ll",
          color: "white",
        },
        title: {
          display: true,
          text: "Date",
          color: "white",
        },
        ticks: {
          color: "white",
        },
      },
      y: {
        min: -1,
        max: 1,
        title: {
          display: true,
          text: "Sentiment Score",
          color: "white",
        },
        ticks: {
          stepSize: 0.5,
          color: "white",
        },
      },
    },
  };

  return (
    chartData.datasets.length > 0 ? (
      <div
        style={{
          display: "flex",
          height: isFullScreen ? "100vh" : "95%",
          width: isFullScreen ? "100vw" : "95%",
          position: isFullScreen ? "fixed" : "relative",
          top: isFullScreen ? 0 : "auto",
          left: isFullScreen ? 0 : "auto",
          zIndex: isFullScreen ? 1000 : "auto",
          padding: isFullScreen ? "20px" : "0",
          backgroundColor: isFullScreen ? "rgba(0, 0, 0, 0.95)" : "transparent",
          justifyContent: "center",
          alignItems: "center",
          borderRadius: isFullScreen ? "0" : "10px",
        }}
      >
        <button
          onClick={() => setIsFullScreen(true)}
          style={{
            position: "absolute",
            top: "10px",
            right: "10px",
            background: "transparent",
            color: "white",
            border: "none",
            fontSize: "20px",
            cursor: "pointer",
            zIndex: 2000,
          }}
        >
          <FaExpandArrowsAlt />
        </button>
  
        {isFullScreen && (
          <button
            onClick={() => setIsFullScreen(false)}
            style={{
              position: "absolute",
              top: "10px",
              right: "50px",
              background: "transparent",
              color: "white",
              border: "none",
              fontSize: "30px",
              padding: "5px",
              cursor: "pointer",
              zIndex: 2001,
            }}
          >
            <TiArrowMinimise />
          </button>
        )}
  
        <button
          onClick={clearChart}
          style={{
            position: "absolute",
            top: "10px",
            left: "10px",
            background: "transparent",
            color: "purple",
            border: "none",
            fontSize: "20px",
            cursor: "pointer",
            zIndex: 2000,
          }}
        >
          <GrClear />
        </button>
  
        <div style={{ flex: 1, width: "100%", height: "100%" }}>
          <Line data={chartData} options={options} ref={chartRef} />
        </div>
      </div>
    ) : null
  );
  
};

export default SentimentChart;
