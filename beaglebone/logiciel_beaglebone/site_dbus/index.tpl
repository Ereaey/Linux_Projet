<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN">
<html>
<head>
  <title>{{title}}</title>
  <link href='https://fonts.googleapis.com/css?family=Open+Sans:400,700,600' rel='stylesheet' type='text/css'>
  <link rel="stylesheet" type="text/css" href="static/design.css">
</head>
<body>

<!-- Navbar -->

<ul class="navbar">
	<div class="logo">Domotique</div>
 	<li><a href="/">Home page</a></li>
 	<li><a href="log">Log</a></li>
</ul>
<!-- Menu gauche --><div class="test">
<div class="menu">
	%for x in menu:
		<button onclick="location.href='draw/{{x['name']}}'">{{x["name"]}}</button>
	%end
</div>

<!-- Main content -->
<div class="content">
	<div class="main">
		<div class="main-bot">
		    <div class="main-texte">Draw</div>
		</div>
		<canvas id="mon_canvas" width="360" height="360" style="border-right: 1px solid black; background-color: rgb(100, 100, 100); float: left;"> 
  Texte alternatif pour les navigateurs ne supportant pas Canvas.
</canvas>
		<div style="float: left;">
			<button onclick="reset();">Reset</button><br />
			<button onclick="send();">Send</button>
		</div>
	</div>
</div>
</div>
<script type="text/javascript">
var tab = new Array();
  var c = document.getElementById("mon_canvas");
  var ctx = c.getContext("2d");
  // Le reste du script ici...
  ctx.beginPath();
ctx.stroke();
function getCoords(el,event) {
  var ox = -el.offsetLeft,
  oy = -el.offsetTop;
  while(el=el.offsetParent){
    ox += el.scrollLeft - el.offsetLeft;
    oy += el.scrollTop - el.offsetTop;
  }
  return {x:event.clientX + ox , y:event.clientY + oy};
}
 
 
function reset()
{
	tab.length = 0;
	ctx.clearRect(0, 0, 360, 360); 
	ctx.beginPath();
}
// Exemple d'utilisation :
 
mon_canvas.onclick = function(e) {
  var coords = getCoords(this,e);
  ctx.lineTo(coords.x,coords.y);
  a = new Array(coords.x,coords.y);
  tab[tab.length] = a;
  ctx.stroke();
};

function send()
{
	
}
</script>

</body>