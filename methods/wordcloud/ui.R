library(shiny)

fluidPage(
  titlePanel("Wordcloud of functional words"),
  selectInput(
    "selectDataset",
    label = "Dataset",
    choices = c("Jane Austen, Emma",
                "Jane Austen, Pride and Prejudice",
                "Charles Dickens, A Christmas Carol",
                "Charles Dickens, Oliver Twist",
                "William Shakespeare, Hamlet",
                "William Shakespeare, Romeo and Juliet",
                "Mark Twain, Adventures of Huckleberry Finn",
                "Mark Twain, The Adventures of Tom Sawyer"),
    multiple = F
  ),
  plotOutput("wordcloud", height = "800px")
)

