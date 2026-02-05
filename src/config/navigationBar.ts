// Navigation Bar
// ------------
// Description: The navigation bar data for the website.
export interface Logo {
	src: string
	alt: string
	text: string
}

export interface NavSubItem {
	name: string
	link: string
}

export interface NavItem {
	name: string
	link: string
	submenu?: NavSubItem[]
}

export interface NavAction {
	name: string
	link: string
	style: string
	size: string
}

export interface NavData {
	logo: Logo
	navItems: NavItem[]
	navActions: NavAction[]
}

export const navigationBarData: NavData = {
	logo: {
		src: '/activate-your-voice-main-logo.png',
		alt: 'Activate Your Voice',
		text: ''
	},
	navItems: [
		{ name: 'Home', link: '/' },
		{ name: 'Team', link: '/the-team' },
		{
			name: 'Vocal Tuition',
			link: '/vocal-tuition',
			submenu: [
				{ name: 'Public Speaking Training & Presentations', link: '/public-speaking' },
				{ name: 'Vocal Coaching', link: '/vocal-coaching' },
				{ name: 'Elocution Lessons / Elocution Courses', link: '/elocution' }
			]
		},
		{
			name: 'Acting Tuition',
			link: '/acting-tuition',
			submenu: [
				{ name: 'Acting Coaching', link: '/acting-coaching' },
				{ name: 'Auditions', link: '/auditions' },
				{ name: 'Speech & Drama Coaching', link: '/speech-drama' },
				{ name: 'Exams & Qualifications', link: '/exams-qualifications' }
			]
		},
		{
			name: 'Corporate',
			link: '/corporate',
			submenu: [
				{ name: 'Business Coaching', link: '/business-coaching' },
				{ name: 'Public Speaking Training & Presentations', link: '/public-speaking-corporate' }
			]
		},
		{ name: 'News', link: '/blog' },
		{
			name: 'Other',
			link: '#',
			submenu: [
				{ name: 'FAQs', link: '/faq' },
				{ name: 'Terms and Conditions', link: '/terms' },
				{ name: 'Privacy Policy', link: '/privacy-policy' },
				{ name: 'Feedback', link: '/feedback' }
			]
		}
	],
	navActions: [{ name: 'Get in touch', link: '/contact', style: 'primary', size: 'lg' }]
}
