# re-place

An attempt to re-create what happened at [r/place](https://www.reddit.com/r/place)

The grid is 1001x1001 because each "pixel" is 1x1 and if a pixel is placed at
(1000, 1000), due to the create_rectangle function, its bottom right corner
would be located at (1001, 1001)

The data file needed for this program (included) was taken from [here](https://mega.nz/#!E0gQ2KiY!n6HnDfR8bpQz79fKv4GtTt06S4iLSBq7bDfeo-rxuUU)
, which is from [this post](https://www.reddit.com/r/place/comments/65x14m/place_time_lapse_and_data_from_start_to_finish/)
.

The structure of the data file is `(time_stamp, user_hash, x_coordinate, y_coordinate, color)`

---

"1.2 million redditors used these premises to build the largest collaborative
art project in history, painting (and often re-painting) the million-pixel
canvas with 16.5 million tiles in 16 colors."
