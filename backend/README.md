# Fact Checker Backend

The backend for the Fact Checker application, responsible for processing articles, running machine learning models, and utilizing a web crawler to determine the authenticity of input articles.

## Overview

The backend performs the following tasks:

- **Web Crawling**: Searches for the original source of the input article.
- **Machine Learning Models**: Analyzes the content of the article to classify it as fake, hoax, propaganda, satire, or trusted news.
- **API Services**: Provides endpoints for the frontend to interact with the backend.

## Features

- **Web Crawler**: Automatically retrieves the original source of the article.
- **ML Models**: Uses trained machine learning models to classify articles on a credibility scale.
- **RESTful API**: Exposes endpoints for article submission and result retrieval.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/aditya06121/fact_checker.git
   ```

2. Navigate to the backend directory:

   ```bash
   cd fact_checker/backend
   ```

3. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Set up environment variables:
   - Create a `.env` file in the backend directory.
   - Add necessary configurations such as API keys, database credentials, etc.

## Usage

1. Start the backend server:

   ```bash
   python main.py
   ```

2. The backend will expose RESTful API endpoints for the frontend to interact with.

## API Endpoints

- **POST /analyze**: Accepts an article or URL and returns the credibility score.
- **GET /source**: Retrieves the original source of the article using the web crawler.

## License

This project is licensed under the MIT License.
