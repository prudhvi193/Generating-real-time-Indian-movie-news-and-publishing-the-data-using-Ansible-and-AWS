#!/usr/bin/python
#Importing flask module for creating a flask web application
from flask import Flask, render_template
#Importing news api module for generating the latest news
from newsapi import NewsApiClient

app = Flask(__name__);

# Create a route function and render the html template on that
@app.route("/")
def main_page():
    #Deails of Client ID and API Key for Authorization Access
    api_key = "e25ddcbc04db44fdaf1878a64c862668"
    newsapi = NewsApiClient(api_key=api_key)
    
    # For getting details of top headlines
    top_headlines = newsapi.get_top_headlines(sources="the-times-of-india")
    
    # For gettind details of all the articles for the top headline news
    top1_articles = top_headlines['articles']

    # List of contents to store the value of that list
    author1 = []
    news1 = []
    description1 = []
    image1 = []
    published_date1= []
    article_link1 = []
    
     # Fetch all the contents of the article's top headlines by using for loop
    for a in range(len(top1_articles)):
        focused_articles = top1_articles[a]
        
        # Append the contents in each of the list
        author1.append(focused_articles['author'])
        news1.append(focused_articles['title'])
        description1.append(focused_articles['description'])
        image1.append(focused_articles['urlToImage'])
        published_date1.append(focused_articles['publishedAt'])
        article_link1.append(focused_articles['url'])
        
        # Create a zip folder to find the top content information directly and easily
        zip_contents = zip(author1,news1,description1,image1,published_date1,article_link1)
        
    # For getting the details of all the main article news
    complete_articles = newsapi.get_everything(q="cinema",sources="the-times-of-india",sort_by="popularity")
    
    # For getting all the articles of the news
    complete1_articles = complete_articles['articles']
    
    # List of content to store value of those lists
    complete_authors = []
    complete_news = []
    complete_description = []
    complete_images = []
    complete_published_dates = []
    complete_article_links = []
    
    # Fetch all the contents of the article's top news for all the articles
    for b in range(len(complete1_articles)):
        complete_focused_articles = complete1_articles[b]
        
        # Append all the contents into each of the lists
        complete_authors.append(complete_focused_articles['author'])
        complete_news.append(complete_focused_articles['title'])
        complete_description.append(complete_focused_articles['description'])
        complete_images.append(complete_focused_articles['urlToImage'])
        complete_published_dates.append(complete_focused_articles['publishedAt'])
        complete_article_links.append(complete_focused_articles['url'])
        
        # Create a zip folder to find the complete content details directly and easily
        complete_zip_contents = zip(complete_authors,complete_news,complete_description,complete_images,complete_published_dates,complete_article_links)
    
    # Pass the zip file in rendered_template
    return render_template('home.html',zip_contents=zip_contents,complete_zip_contents=complete_zip_contents)

# The main function to debug the developed flask app
if __name__ == "__main__":
    app.run(debug=True)
