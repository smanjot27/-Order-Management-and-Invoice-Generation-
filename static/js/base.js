function display()
{
	var elem=document.getElementById('alert');
	elem.style.display='none';
}

function track(checkbox)
{
	if(checkbox.checked==true)
	{
		document.getElementById('del').removeAttribute('disabled');
	}
	else
	{
		document.getElementById('del').setAttribute('disabled','disabled');
	}

}
