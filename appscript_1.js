function doGet(request) {
   var query = request.parameter.q;
   var parameter = 2;
   var sheetname = "Sheet1";
   var doc = SpreadsheetApp.openById(PropertiesService.getScriptProperties().getProperty("key"));
   var sheet = sheet.getLastRow();
   var rows = [];
   var range = sheet.getRange(2, 1, nextRow, parameters);
   var values = range.getValues();
   for (var row in values) {
      rows.push([]);
      for (var col in values[row]) {
         rows[row].push(values[row][col]);
      }
   }
   if (query != null) {
      var rowstoreturn = rows.filter(a => a[0] == query)
      return ContentService
         .createTextOutput(JSON.stringify({ 'data': rowstoreturn, 'error': false }))
         .setMimeType(ContentService.MimeType.JSON);
   }
   return ContentService
      .createTextOutput(JSON.stringify({ 'data': rows, 'error': false }))
      .setMimeType(ContentService.MimeType.JSON);
   function setup() {
      var doc = SpreadsheetApp.getActiveSpreadsheet();
      PropertiesService.getScriptProperties().setProperty("key", doc.getId());
   }
}