These files create word cloud for discriminative functional words ***selected by the object*** `dws_mask.R`. 

`wordcloud.rmd` contains the code creating a word cloud for a given book.

`server.R` and `ui.R` further create a [ShinyApp](https://kirin.shinyapps.io/wordcloud/) to allow users to select books. We need to put them under the same directory as `dataset`. That is why we copy `dataset` here.
