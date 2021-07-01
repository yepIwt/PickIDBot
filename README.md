# Pick ID Bot

## _Receiving the sent type ID_

If you want to find out the `file id` of a document or photo in a telegram, then *just send it to the bot*

### Example

![](https://i.imgur.com/kOchhd3.png)

## Docker

Insert Telegram bot token into `Dockerfile`. Run these commands:
```sh
docker build -t picker .
docker run --name PickIDBot -d picker
```
