# not very optimized.
# the only optimization right now is to search
# only in one triangle of {100, ..., 999}^2 since a*b = b*a.

is_pal <- function(n) {
  s <- strsplit(as.character(n), '')[[1]]
  all(s == rev(s))
}

palfinder <- function() {
  pals <- matrix(0,5000,3)  # known to be big enough
  k <- 1
  for(i in 999:100) {
    for(j in i:100) {
      n = i * j
      if(is_pal(n)) {
        pals[k,] <- c(i,j,n)
        k <- k + 1
      }
        
    }
  }
  pals[1:k,]
}

pp = palfinder()
print(max(pp[,3]))

