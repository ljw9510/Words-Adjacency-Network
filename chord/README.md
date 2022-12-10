These files create chord diagrams for ***all*** functional words. 

`chord_uu.rmd` contains the code creating a chord diagram for a given book.

`server.R` and `ui.R` further create a [ShinyApp](https://kirin.shinyapps.io/chord/) to allow users to select books. We need to put them under the same dictionary as `dataset`. That is why we copy `dataset` here.
