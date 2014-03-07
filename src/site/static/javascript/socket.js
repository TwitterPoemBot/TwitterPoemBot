var url = "https://stream.twitter.com/1.1/statuses/sample.json";
var accessor = {
    oauth_consumer_key: "15Cr8pcLsZQJFfMBjJegw", 
    oauth_token: "2377663207-eqs7DsG2nZX6KjfCVELXeEKUFeqNrpalGilpavU",
    oauth_version : "1.0",
    tokenSecret: "Gcj7cnvQXkoYnfc48G0sTXBPRap15kk689N8ZeteYRtYX",
};

var message = {
  action: url,
  method: "GET",
  parameters: {}
};

OAuth.completeRequest(message, accessor);        
OAuth.SignatureMethod.sign(message, accessor);
url = url + '?' + OAuth.formEncode(message.parameters);

var messageLen = 0;

var xhr = new XMLHttpRequest();
xhr.open('GET', url, true);

xhr.onreadystatechange = function() {
  if(xhr.readyState == 2 && xhr.status == 200) {
     // Connection is ok
  } else if(xhr.readyState == 3){ 
  //Receiving stream
  if (messageLen < xhr.responseText.length){
    alert(messageLen +"-"+ xhr.responseText.length +":"+xhr.responseText.substring(messageLen,xhr.responseText.length));
  }
  messageLen = xhr.responseText.length;                     
  }else if(xhr.readyState == 4) {}    
  // Connection completed
};  
xhr.send();
