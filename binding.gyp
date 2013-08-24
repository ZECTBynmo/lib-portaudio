{
	"conditions" : [
		# OSX
		# 1) use the portaudio configure
		# 2) make
		[ 'OS!="win"', {
			'targets': [
				{
					'target_name': 'Configure',
					'type': 'loadable_module',
					'actions': [{
						'action_name': 'Configure',
						'inputs': ['./configure'],
						'action': [
							'./configure'
						],
						'outputs': ['dummy'],
					}]
				},
				{
					'target_name': 'Make',
					'type': 'loadable_module',
					'actions': [{
						'action_name': 'make',
						'inputs': ['./configure'],
						'action': [
							'make'
						],
						'dependencies': [
							'Configure',
						],
						'outputs': ['dummy'],
					}]
				},
			]}
		],
		[ 'OS=="win"', {
			'targets': [
				{
					'target_name': 'DoNothing',
					'type': 'loadable_module',
					'msvs_guid': '7552114E-A692-4323-A889-B44662348376',
				},
			]}
		]
	]
}