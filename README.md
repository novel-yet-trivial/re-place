# re-place

An attempt to re-create what happened at [r/place](https://www.reddit.com/r/place)

The grid is 1001x1001 because each "pixel" is 1x1 and if a pixel is placed at
(1000, 1000), due to the create_rectangle function, its bottom right corner
would be located at (1001, 1001)

The data file needed for this program can be found [here](https://www.reddit.com/r/redditdata/comments/6640ru/place_datasets_april_fools_2017/)
under the `Datasets` header, under `Full dataset` download the [zipped csv](https://storage.googleapis.com/place_events/tile_placements.csv.gz)
and then extract it to the same directory as `re-place.py`

The structure of the data file is `(time_stamp, user_hash, x_coordinate, y_coordinate, color)`

---

"1.2 million redditors used these premises to build the largest collaborative
art project in history, painting (and often re-painting) the million-pixel
canvas with 16.5 million tiles in 16 colors."
