$('#calendar').fullCalendar({
			header: {
				left: 'today prev,next',
				center: 'title',
				right: 'month,agendaWeek,agendaDay'
			},
			defaultDate: '2016-10-12',
			navLinks: true, // can click day/week names to navigate views

			weekNumbers: false,
			weekNumbersWithinDays: true,
			weekNumberCalculation: 'ISO',

			editable: true,
			eventLimit: false, // allow "more" link when too many events
			events: [
				{
					title: '10:00 am Delegate Tony Wilt’s Fifth Annual Sporting Clays Shoot',
					start: '2016-10-01'
				},
                {
					title: '12:00 pm Delegate Jeoin Ward Luncheon',
					start: '2016-10-04'
				},
                {
					title: '3:00 pm Delegate Jim LeMunyon Fundraising Lunch Reception',
					start: '2016-10-04'
				},
                {
					title: '12:00 pm Delegate Jeoin Ward Luncheon',
					start: '2016-10-06'
				},
                {
					title: '3:00 pm Delegate Jim LeMunyon Fundraising Lunch Reception',
					start: '2016-10-06'
				},
				{
					title: '10:00 am Delegate Tony Wilt’s Fifth Annual Sporting Clays Shoot',
					start: '2016-10-09T16:00:00'
				},
				{
					title: '12:00 pm Delegate Jeoin Ward Luncheon',
					start: '2016-10-14'
				},
				{
					title: '3:00 pm Delegate Jim LeMunyon Fundraising Lunch Reception',
					start: '2016-10-14'
				},
				{
					title: '10:00 am Delegate Tony Wilt’s Fifth Annual Sporting Clays Shoot',
					start: '2016-10-15'
				},
				{
					title: '12:00 pm Delegate Jeoin Ward Luncheon',
					start: '2016-10-17'
				},
				{
					title: '3:00 pm Delegate Jim LeMunyon Fundraising Lunch Reception',
					start: '2016-10-17'
				},
				{
					title: '10:00 am Delegate Tony Wilt’s Fifth Annual Sporting Clays Shoot',
					start: '2016-10-23'
				},
				{
					title: '3:00 pm Delegate Jim LeMunyon Fundraising Lunch Reception',
					start: '2016-10-26'
				},
				{
					title: '6:00 pm Senator Amanda Chase Evening Reception',
					start: '2016-10-26'
				},
				{
					title: '12:00 pm Delegate Jeoin Ward Luncheon',
					start: '2016-10-28'
				},
				{
					title: '10:00 am Delegate Tony Wilt’s Fifth Annual Sporting Clays Shoot',
					start: '2016-10-30'
				},
				{
					title: '3:00 pm Delegate Jim LeMunyon Fundraising Lunch Reception',
					start: '2016-10-31'
				},
				{
					title: '12:00 pm Delegate Jeoin Ward Luncheon',
					start: '2016-10-31'
				},
				{
					title: 'Birthday Party',
					start: '2016-10-13T07:00:00'
				},
                {
					title: 'Meeting',
					start: '2016-10-19T10:30:00',
					end: '2016-10-12T12:30:00'
				},
				{
					title: 'Lunch',
					start: '2016-10-19T12:00:00'
				},
			]
		});