function googleTranslateElementInit() {
  new google.translate.TranslateElement({pageLanguage: 'en'}, 'google_translate_element');
}

function table_ele(){
    var cur_dat = document.getElementById('table_content').innerHTML;
    var tags_pair = ['<tr>','</tr>','<td>','</td>'];
    document.getElementById('table_content').innerHTML = cur_dat + tags_pair[0]+tags_pair[2]+document.getElementById("fac_name").value+tags_pair[3]+tags_pair[2]+document.getElementById("fac_desig").value+tags_pair[3]+tags_pair[2]+document.getElementById("fac_dom").value+tags_pair[3]+tags_pair[2]+document.getElementById("fac_Email").value+tags_pair[3]+tags_pair[1];
    return false; 
}

function loadXMLDoc() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var xmlDoc = this.responseXML;
            constructTable(xmlDoc);
        }
    };
    xhttp.open("GET", "test.xml", true);
    xhttp.send();
}

function constructTable(xmlDoc){
    //here we construct the table doc.
    var text = "";
    alert("Iam here!");
    var temp = xmlDoc.getElementsByTagName("name")[0].childNodes;
    document.getElementById("table_content").innerHTML+= temp[0].nodeValue;
    
    return;
}