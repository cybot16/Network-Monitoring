$('.message a').click(function(){
   $('form').animate({height: "toggle", opacity: "toggle"}, "slow");
});
	var el = document.getElementById("customize");
	var ic = document.getElementById('icodir');
	var lb = document.getElementById('label');
	lb.innerHTML = 'Open panel';
	setTimeout('opend()',500);
	function opend(){
		var b = '';
		var max = 200;
		var a = el.clientHeight;
		if(a>=max){
			b = '25px';
			setTimeout('addCla("dispview up","Open panel")',100);
		}else{
			b = '50px';
			setTimeout('addCla("dispview","Close panel")',100);
		}

		el.style.height = b;
	}
	function addCla(pass1,pass2){
		ic.className = pass1;
		lb.innerHTML = pass2;
	}