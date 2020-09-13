$(window).on("load", function() {
  var column = $(".spg-video-column");
  var icons = $(".spg-feed-icons");
  var twitter = $(".twitter-timeline");
  twitter.height(column.height() - icons.height());
  twitter.css("height", column.height() - icons.height());
});
