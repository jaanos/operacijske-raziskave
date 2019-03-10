install.packages(c('repr', 'IRdisplay', 'evaluate', 'crayon', 'pbdZMQ', 'devtools', 'uuid', 'digest'), repos="https://cran.rstudio.com/")
devtools::install_github('IRkernel/IRkernel')
IRkernel::installspec()
