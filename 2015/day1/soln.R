find_floor <- function(instructions) {
  floor <- 0
  for (char in strsplit(instructions, "")[[1]]) {
    if (char == "(") {
      floor <- floor + 1
    } else if (char == ")") {
      floor <- floor - 1
    }
  }
  return(floor)
}

find_basement_position <- function(instructions) {
  floor <- 0
  for (i in 1:nchar(instructions)) {
    char <- substr(instructions, i, i)
    if (char == "(") {
      floor <- floor + 1
    } else if (char == ")") {
      floor <- floor - 1
    }
    if (floor == -1) {
      return(i)
    }
  }
  return(NULL)
}

instructions <- readLines("input.txt")
instructions <- paste(instructions, collapse = "")

floor <- find_floor(instructions)
cat("Part 1: Final floor:", floor, "\n")

basement_position <- find_basement_position(instructions)
cat("Part 2: First basement position:", basement_position, "\n")

