CREATE TABLE search_metadata (
    search_metadata_id SERIAL PRIMARY KEY,
    user_id INT,
    search_term VARCHAR(255) NOT NULL,
    searched_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE search_results (
    search_result_id SERIAL PRIMARY KEY,
    search_term VARCHAR(255),
    mean_sentiment DECIMAL(5, 2),
    positive_article_count INT,
    negative_article_count INT,
    total_article_count INT,
    ratio_positive_vs_negative DECIMAL(5, 2),
    main_headline VARCHAR(4000),
    top_3_articles JSONB,
    bottom_3_articles JSONB,
    created_at TIMESTAMP DEFAULT NOW() 
);