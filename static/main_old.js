function myfunction() {
   alert("MAAP BANG BELOM BIKIN")
}

const rupiah = (number)=>{
    return new Intl.NumberFormat("id-ID", {
      style: "currency",
      currency: "IDR"
    }).format(number);
  }

function Sept() {
   var table = document.getElementById("tableId");
   var rows =   parseInt(document.getElementById("value1").innerHTML);
   var rows2 =  parseInt(document.getElementById("value2").innerHTML);
   var rows3 =  parseInt(document.getElementById("value3").innerHTML);
   var rows4 =  parseInt(document.getElementById("value4").innerHTML);
   console.log(rows+rows2+rows3+rows4)
   var Total = rows+rows2+rows3+rows4
   return rupiah(Total);    
};


console.log(rupiah(20000))
document.getElementById('totalvalue').innerHTML = Sept();


