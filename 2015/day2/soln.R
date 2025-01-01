calculate_wrapping_paper_and_ribbon <- function(dimensions) {
  total_paper <- 0
  total_ribbon <- 0
  
  for (dim in dimensions) {
    dims <- as.numeric(strsplit(dim, "x")[[1]])
    
    if (length(dims) != 3 || any(is.na(dims))) {
      print("Invalid dimensions found!")
      next
    }
    
    l <- dims[1]
    w <- dims[2]
    h <- dims[3]
    
    surface_area <- 2 * (l * w + w * h + h * l)
    smallest_side <- min(l * w, w * h, h * l)
    total_paper_for_present <- surface_area + smallest_side
    total_paper <- total_paper + total_paper_for_present
    
    smallest_perimeter <- 2 * (min(l + w, w + h, h + l))
    volume <- l * w * h
    total_ribbon_for_present <- smallest_perimeter + volume
    total_ribbon <- total_ribbon + total_ribbon_for_present
  }
  
  return(c(total_paper, total_ribbon))
}

dimensions <- readLines("input.txt")

dimensions <- trimws(dimensions)
dimensions <- dimensions[dimensions != ""]

totals <- calculate_wrapping_paper_and_ribbon(dimensions)

cat("Total square feet of wrapping paper needed:", totals[1], "\n")
cat("Total feet of ribbon needed:", totals[2], "\n")

