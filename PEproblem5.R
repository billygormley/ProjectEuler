mysteryNumber <- 21
sequenceLength <- 20

sequenceNumber <- seq(1:sequenceLength)
sequenceCheck <- rep(0,sequenceLength)

sum(sequenceCheck)

while (sum(sequenceCheck != sequenceLength)) {
	
	#Reset numbers in sequenceCheck vector
	sequenceCheck <- rep(0,sequenceLength)

	#Run through for loop to assign values for sequenceCheck
	#based on the divisibility of sequenceNumber on myseryNumber
	for (i in sequenceNumber) {
		if (mysteryNumber %% sequenceNumber[i] == 0) {
			sequenceCheck[i] <- 1
		}
	}

	if (sum(sequenceCheck) == sequenceLength) {
		break
	}
	
	mysteryNumber <- mysteryNumber + 1
}

sum(sequenceCheck)

df <- data.frame(sequenceNumber, sequenceCheck)
df

mysteryNumber