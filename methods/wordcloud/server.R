library(shiny)
library(wordcloud)

function(input, output) {
  freq <- reactive({
    book_names = c("austen_2", 
                   "austen_4", 
                   "dickens_1", 
                   "dickens_4",
                   "shakespeare_1",
                   "shakespeare_5",
                   "twain_1",
                   "twain_4")
    
    book_fullnames = c("Jane Austen, Emma",
                       "Jane Austen, Pride and Prejudice",
                       "Charles Dickens, A Christmas Carol",
                       "Charles Dickens, Oliver Twist",
                       "William Shakespeare, Hamlet",
                       "William Shakespeare, Romeo and Juliet",
                       "Mark Twain, Adventures of Huckleberry Finn",
                       "Mark Twain, The Adventures of Tom Sawyer")
    filePath <- paste0("./dataset/", book_names[book_fullnames == input$selectDataset] , ".txt")
    word_list = read.table("./dataset/functionwords_list.txt", head=FALSE)
    word_list <- as.matrix(word_list)
    
    book = read.table(filePath, head=FALSE)
    colnames(book) = word_list
    row.names(book) = word_list
    load("./dws_mask.R")
    book <- book[dws_mask, dws_mask]
    diag(book) <- 0
    book <- as.matrix(book)
    idx <- (rowSums(book) != 0) | (colSums(book) != 0)
    book <- book[idx, idx]
    book_freq <- rowSums(book)
    book_freq
  })
  
  output$wordcloud <- renderPlot(
    wordcloud(words = names(freq()), 
              freq = freq(), 
              scale = c(10, 1),
              min.freq = 1, 
              max.words=200, 
              random.order=FALSE, 
              rot.per=0.35, 
              colors=brewer.pal(8, "Dark2")))
}
