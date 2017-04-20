# re-place

An attempt to re-create what happened at [r/place](https://www.reddit.com/r/place)

The data file needed for this program (included) was taken from [here](https://mega.nz/#!E0gQ2KiY!n6HnDfR8bpQz79fKv4GtTt06S4iLSBq7bDfeo-rxuUU)
, which is from [this post](https://www.reddit.com/r/place/comments/65x14m/place_time_lapse_and_data_from_start_to_finish/)
.

The binary data file uses 3 bytes (24 bits) per pixel. Each pixel is saved as a int24 little endian which is (10 bit uint X), (10 bit uint Y), (4 bit uint color).

The data comprises 16,556,641 pixels changes. X and Y are in the range 0 - 999 (inclusive). color is in the range 0 - 15 (inclusive). 3,256 pixels were removed from the original dataset as they were out of range; presumibly due to data sanitation error.

---

"1.2 million redditors used these premises to build the largest collaborative
art project in history, painting (and often re-painting) the million-pixel
canvas with 16.5 million tiles in 16 colors."
