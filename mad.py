// -0dconsole.log('hi')

const Discord = require('discord.js')
const client = new Discord.Client()
const beany = '162330485714845696'
const fs = require('fs')
const request = require('request') // REQUIRE request. Similar to import in python.
var prefix = '!' // prefix for stuff lol
var globalChannel;
var newErrors; 

var oldErrors;
//var channel = "351520153634078721"






client.on('ready', () => { // On ready, do this!
  globalChannel = client.channels.get('345614200523063297')
  console.log(`[DISCORD] Logged in as ${client.user.tag}!`);
})



function messageErrorChange () {
  globalChannel.send('ErorrTest')
};



setInterval(function jsonGrab () {
  
  console.log('Grabbing JSON from https://analyticord.solutions/api/error?error=list')

  var requestgrab = request('https://analyticord.solutions/api/error?error=list')

  request('https://analyticord.solutions/api/error?error=list', function (error, response, body) {
    if (error) { console.log('[FATAL] Error:', error) }// Print the error if one occurred
    console.log('[REQUEST] statusCode:', response && response.statusCode)
      // console.log('body:', body); // Print the HTML for the Google homepage.
    fs.writeFile('errorlist.txt', body)
    errorChecker();
  })
}, 10000)


function errorChecker() {

newErrors = request('https://analyticord.solutions/api/error?error=list', function (error, response, body) {});

if (oldErrors == newErrors) {console.log('No new errors.')} 

oldErrors = fs.readFile('errorlist.txt', function read (err, data) {
  if (err) { console.log('[FATAL] Error at jsonCheck:', err)
  if (newErrors !== data ) { messageErrorChange(), console.log(data)} }
} );

}
  







client.login(nah')
