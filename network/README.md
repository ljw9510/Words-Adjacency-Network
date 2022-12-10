These files create force networks for discriminative functional words selected by the object `dws_mask.R`. 

`network.rmd` contains the code creating a force network for a given book.

`server.R` and `ui.R` further create a [ShinyApp](https://kirin.shinyapps.io/network/) to allow users to select books. We need to put them under the same dictionary as `dataset`. That is why we copy `dataset` here.
