// function to search in the table with id="tblId" and search string="inputVal"
function searchTable(inputVal, tblId) {
	var table = $(tblId);
	table.find('tr').each(function(index, row) {
		var allCells = $(row).find('td');
		if(allCells.length > 0) {
			var found = false;
			allCells.each(function(index, td) {
				var regExp = new RegExp(inputVal, 'i');
				if(regExp.test($(td).text())) {
					found = true;
					return false;
				}
			});
			if(found == true)
				$(row).show();
			else
				$(row).hide();
		}
	});
}