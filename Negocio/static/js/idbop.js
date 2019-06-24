/*
fetch('https://pardob.pythonanywhere.com/perros/', { 
	method: 'GET', 
	headers: new Headers({
	  'Authorization': 'Token 8f907480d6257ceb509db9e6fb34c97793ee39a3', 
	}), 
  })
*/

		////
		//

		var dbPromise = idb.open('feeds-db', 5, function(upgradeDb) {
			upgradeDb.createObjectStore('feeds',{keyPath:'pk'});
		});
		//collect latest post from server and store in idb.
		fetch('https://pardob.pythonanywhere.com/perros/', { 
			method: 'GET', 
			headers: new Headers({
	  			'Authorization': 'Token 8f907480d6257ceb509db9e6fb34c97793ee39a3', 
			}), 
  		  }).then(function(response){
			return response.json();
		}).then(function(jsondata){
			console.log(jsondata)
			dbPromise.then(function(db){
				var tx = db.transaction('feeds', 'readwrite');
					var feedsStore = tx.objectStore('feeds');
					for(var key in jsondata['results']){
						console.log(key);
						
						feedsStore.put(jsondata['results'][key]);	
						
					}
			});
		});
		//retrive data from idb and display on page.
		var post="";
		dbPromise.then(function(db){
			var tx = db.transaction('feeds', 'readonly');
				var feedsStore = tx.objectStore('feeds');
				return feedsStore.openCursor();
		}).then(function logItems(cursor) {
				if (!cursor) {
					//if true means we are done cursoring over all records in feeds.
					document.getElementById('offlinedata').innerHTML=post;
					return;
				}
				for (var field in cursor.value) {
						if(field=='fields'){
							feedsData=cursor.value[field];
							for(var key in feedsData){
								if(key =='title'){
									var title = '<h3>'+feedsData[key]+'</h3>';
								}
								if(key =='author'){
									var author = feedsData[key];
								}
								if(key == 'body'){
									var body = '<p>'+feedsData[key]+'</p>';
								}	
							}
							post=post+'<br>'+title+'<br>'+author+'<br>'+body+'<br>';
						}
					}
				return cursor.continue().then(logItems);
			});