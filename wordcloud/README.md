These files create word cloud for functional words. 

`wordcloud.rmd` contains the code creating a word cloud for a given book.

`server.R` and `ui.R` further create a [ShinyApp](https://kirin.shinyapps.io/network/) to allow users to select books. We need to put them under the same dictionary as `dataset`. That is why we copy `dataset` here.
