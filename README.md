# polo-web-scraper
python program that scrapes websites for polopicker

important links:
how to find sitemap: https://writemaps.com/blog/how-to-find-your-sitemap/
import sitemap links: https://docs.google.com/spreadsheets/d/1JPsh4d7gZjaLEFXo2jd4A2UA3sw845UeYk_23KWqd3w/edit#gid=1429691697
get all links from web page: https://towardsdatascience.com/quickly-extract-all-links-from-a-web-page-using-javascript-and-the-browser-console-49bb6f48127b

var x = document.querySelectorAll("a");
var myarray = []
for (var i=0; i<x.length; i++){
var nametext = x[i].textContent;
var cleantext = nametext.replace(/\s+/g, ' ').trim();
var cleanlink = x[i].href;
myarray.push([cleantext,cleanlink]);
};
function make_table() {
    var table = '<table><tbody>';
   for (var i=0; i<myarray.length; i++) {
            table += '<tr><td>'+myarray[i][1]+'</td></tr>';
    };

    var w = window.open("");
w.document.write(table);
}
make_table()



maybe useful future links:
https://gist.github.com/niccokunzmann/6038331 : when threads are hanging, this will tell you where
