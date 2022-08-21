function myFunction() {
  /*
  */
  var token = "您的LineNotify"; //Line Notify

  var send_name="新莊高中學聯會";//寄信者名稱  
  var subject="墨墨特約表單填寫成功通知!";  //寄信者標題
  var sheet = SpreadsheetApp.getActiveSheet();
  var lastColumn = sheet.getLastColumn();
  var lastRow=sheet.getActiveCell().getLastRow();
  var message = "";

  for (var i = 1 ; i <= lastColumn; i++) {
    //有填資料才顯示
    if(sheet.getRange(lastRow,i).getValue()!="")
    {
        message += "\n" + sheet.getRange(1,i).getValue() + "：" + sheet.getRange(lastRow,i).getValue() + "<br/>";
    }
  }

  email=sheet.getRange("I"+lastRow).getValue();//使用者email
  message += "<br/>" + "我是會長魏佑丞，本信件為自動回覆，當你看到這封信時不用回信。\n學聯預計於8/25前將優惠券放置於會辦桌上，請再耐心等候🥰\n"
  MailApp.sendEmail({
    name:send_name,
    to: email,
    subject: subject,
    htmlBody: message
  });
  
  message=message.replace(/<br\s*[\/]?>/gi,"\n");//將所有的<br>換成\n
  //傳送到LineNotify
  var options =
  {
     "method"  : "post",
     "payload" : {"message" : message},
     "headers" : {"Authorization" : "Bearer " + token}
  };

  UrlFetchApp.fetch("https://notify-api.line.me/api/notify"
, options);
 

}
