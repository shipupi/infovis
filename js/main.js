

const url_prefix = "makeover/"
let makeovers = [
    {'title': "Week 9 - Seats Held by Women in National Parliaments and Governments", "url": "makeover_week9.html"},
    {'title': "Week 11 - What is the World's Biggest Cash Crop?", "url": "makeover_week11.html"},
    {'title': "Todo", "url": "todo.html"}
]

d3.select("#makeover-list")
    .selectAll("li")
    .data(makeovers)
    .enter()
    .append("li")
    .append("a")
    .text(d => d.title)
    .attr("href", d => url_prefix + d.url);
