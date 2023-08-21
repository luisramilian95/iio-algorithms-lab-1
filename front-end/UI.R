library(shiny)
library(shinydashboard)

# Define UI for application that draws a histogram
dashboardPage(
    dashboardHeader(title = "Algoritmos en la Ciencia de Datos"),
    dashboardSidebar(
        sidebarMenu(
            menuItem("Método de Newton Raphson", tabName = "newtonRaphson"),
            menuItem("Bisección", tabName = "bisection")
        )
    ),
    dashboardBody(
        tabItems(
            tabItem("newtonRaphson",
                    h1("Método de Newton Raphson"),
                    box(textInput("equation", "Ingrese la Ecuación"),
                        textInput("x0", "Solucion Inicial"),
                        textInput("k_max", "K max"),
                        textInput("epsilon", "Error")),
                    actionButton("solveByNewtonRpason", "Resolvolver"),
                    tableOutput("newtonRapshonTable")),
            
            tabItem("bisection",
                    h1("Bisección"),
                    box(textInput("equation", "Ingrese la Ecuación"),
                    textInput("a", "Valor Inicial"),
                    textInput("b", "Valor Final"),
                    textInput("k_max", "K max"),
                    textInput("epsilon", "Error")),
                    actionButton("solveByBisection", "Resolver"),
                    tableOutput("bisectionTable"))
        )
    )
)
