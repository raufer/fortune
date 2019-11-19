# Fortune

## Install instructions


This project has some private dependencies

```bash
pip install git+https://github.com/waymarktech/graphify.git
pip install git+https://github.com/waymarktech/linkify.git
```


## Articles Schema

Each document is represent as a graph in order to capture the structural information.

The following fields are added as top-level fields:

* `url`: The crawling source URL of the article;
* `timestamp`: Article's publishing data in ISO 8601 UTC format
* `author`: The author of the article (url?)
* `title`: Main title of the article
* `meta`: General-purpose path where optional information can be stored


## Resources

* [List of libraries, tools and APIs for web scraping and data processing.](https://github.com/lorien/awesome-web-scraping)
