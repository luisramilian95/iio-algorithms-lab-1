library(shiny)
library(reticulate)

use_python("/Library/Frameworks/Python.framework/Versions/3.10/bin/python3")

py_install("pandas")
py_install("numpy")
py_install("sympy")


setwd("/Users/luisramilian/Documents/Data\ Science\ Master/Trimestre 3/iio-algorithms-lab-1/front-end")

source_python("../back-end/bisection.py")
source_python("../back-end/newton-rapshson.py")


shinyServer(function(input, output) {
  
  newtonRapshonCalculate<-eventReactive(input$solveByNewtonRpason, {
    function_str<-input$equation[1]
    x_0<-as.double(input$x0[1])
    k_max<-as.integer(input$k_max[1])
    epsilon<-as.double(input$epsilon[1])
    outs<-newton_raphson(function_str, x_0, k_max, epsilon)
    return (outs)
  })
  
  bisectionCalculate<-eventReactive(input$solveByBisection, {
    function_str<-input$equation[1]
    a<-as.double(input$a[1])
    b<-as.double(input$b[1])
    k_max<-as.integer(input$k_max[1])
    epsilon<-as.double(input$epsilon[1])
    outs<-bisection(function_str, a,b, k_max, epsilon)
    return (outs)
  })
  
  
  output$newtonRapshonTable<-renderTable({
    newtonRapshonCalculate()
  })
  
  output$bisectionTable<-renderTable({
    bisectionCalculate()
  })
})
