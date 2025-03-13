import { useRef } from 'react';
import { Canvas, useFrame, useLoader } from '@react-three/fiber';
import { Sphere } from '@react-three/drei';
import * as THREE from 'three';
import earthTexture from './globeTexture.png';
import { useNavigate } from 'react-router-dom';

const Globe = ({ position = [0, 0, 0], scale = [2, 2, 2] }) => {
  const globeRef = useRef();
  const texture = useLoader(THREE.TextureLoader, earthTexture);
  const navigate = useNavigate();

  useFrame(() => {
    if (globeRef.current) {
      globeRef.current.rotation.y += 0.003;
    }
  });

  const handleClick = () => {
    navigate('/'); 
  };

  return (
    <Sphere
      ref={globeRef}
      args={[1, 32, 32]}
      position={position}
      scale={scale}
      onClick={handleClick}
      style={{ cursor: 'pointer' }} 
    >
      <meshStandardMaterial map={texture} />
    </Sphere>
  );
};

const GlobeComponent = ({ position, scale, lightSettings = {}, style = {}, canvasProps = {} }) => {
  const defaultLightSettings = {
    ambientLightIntensity: 1.2,
    directionalLightPosition: [1, 5, 5],
  };

  const { ambientLightIntensity, directionalLightPosition } = {
    ...defaultLightSettings,
    ...lightSettings,
  };

  return (
    <div style={{ width: '100%', height: '100%', ...style }}>
      <Canvas style={{ width: '100%', height: '100%' }} {...canvasProps}>
        <ambientLight intensity={ambientLightIntensity} />
        <directionalLight position={directionalLightPosition} />
        <Globe position={position} scale={scale} />
      </Canvas>
    </div>
  );
};

export default GlobeComponent;
