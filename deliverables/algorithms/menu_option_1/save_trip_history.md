###Save Trip History 
Receive the following required information from Menu 1: Date, Origin, Destination, Chosen Path, and Fare.

Check if any required information is missing. If incomplete, do not save the trip and return an error message, "Required information not provided".

Check if `trip_history.csv` exists. If not, prepare an empty list for the first trip.

Use `read_csv()` to retrieve existing trip records if the file exists.

Add the new trip to the existing records.

Use `write_csv()` to save the updated records to `trip_history.csv`, creating the file if necessary.

If saving is successful, display "Trip saved successfully!" Otherwise, display an error message.
