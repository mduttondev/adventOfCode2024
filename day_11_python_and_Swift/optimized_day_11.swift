import Foundation

var stones = [5, 62914, 65, 972, 0, 805922, 6521, 1639064]
let blinks = 75

// Function to process a single stone based on the rules
func processStone(_ stone: Int) -> [Int] {
    if stone == 0 {
        return [1] // Splits into one stone
    } else if String(stone).count % 2 == 0 {
        let stoneString = String(stone)
        let cutPoint = stoneString.count / 2
        let firstHalf = String(stoneString.prefix(cutPoint))
        let secondHalf = String(stoneString.suffix(cutPoint))
        
        if let first = Int(firstHalf), let second = Int(secondHalf) {
            return [first, second] // Splits into two stones
        }
    } else {
        return [stone * 2024] // Transforms into one stone
    }
    return []
}

// Dictionary to track stone values and their counts
var stoneCounts: [Int: Int] = [:]

// Initialize the dictionary with the input stones
for stone in stones {
    stoneCounts[stone, default: 0] += 1
}

// Process stones for the given number of blinks
for _ in 0..<blinks {
    var nextStoneCounts: [Int: Int] = [:]
    
    for (stone, count) in stoneCounts {
        let newStones = processStone(stone)
        for newStone in newStones {
            nextStoneCounts[newStone, default: 0] += count
        }
    }
    
    stoneCounts = nextStoneCounts
}

// Calculate the total number of stones after 75 iterations
let totalStones = stoneCounts.values.reduce(0, +)
print(totalStones)