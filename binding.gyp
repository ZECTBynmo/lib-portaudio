{
	"conditions" : [
		# OSX
		# 1) use the portaudio configure
		# 2) make
		[ 'OS!="win"', {
			'targets': [
				{
					'target_name': 'ConfigurePortAudio',
					'type': 'loadable_module',
					'msvs_guid': '7552114E-A692-4323-A889-B446623E8376',
					'actions': [{
						'action_name': 'Configure and make',
						'action': [
							'./portaudio/configure && make'
						], 
						'outputs': ['dummy'],
					}]
				},
			]}
		],
		[ 'OS=="win"', {
			'targets': [
				{
					'target_name': 'ConfigurePortAudio',
					'type': 'loadable_module',
					'msvs_guid': '7552114E-A692-4323-A889-B446623E8376',
				},
			]}
		]
	]
}