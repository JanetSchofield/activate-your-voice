// Footer Navigation
// ------------
// Description: The footer navigation data for the website.
export interface Logo {
	src: string
	alt: string
	text: string
}

export interface FooterAbout {
	title: string
	aboutText: string
	logo: Logo
}

export interface SubCategory {
	subCategory: string
	subCategoryLink: string
}

export interface FooterColumn {
	category: string
	subCategories: SubCategory[]
}

export interface SubFooter {
	copywriteText: string
}

export interface FooterData {
	footerAbout: FooterAbout
	footerColumns: FooterColumn[]
	subFooter: SubFooter
}

export const footerNavigationData: FooterData = {
	footerAbout: {
		title: 'Activate Your Voice',
		aboutText: '',
		logo: {
			src: '/activate-your-voice-main-logo.png',
			alt: 'Activate Your Voice',
			text: ''
		}
	},
	footerColumns: [
		{
			category: 'Quick Links',
			subCategories: [
				{
					subCategory: 'About Us',
					subCategoryLink: '/the-team'
				},
				{
					subCategory: 'Elocution Lessons',
					subCategoryLink: '/elocution'
				},
				{
					subCategory: 'What is Public Speaking Training?',
					subCategoryLink: '/public-speaking'
				},
				{
					subCategory: 'Privacy Policy',
					subCategoryLink: '/privacy-policy'
				}
			]
		},
		{
			category: 'Contact',
			subCategories: [
				{
					subCategory: 'book@activateyourvoice.co.uk',
					subCategoryLink: 'mailto:book@activateyourvoice.co.uk'
				},
				{
					subCategory: 'Mob : 07779 744353',
					subCategoryLink: 'tel:07779744353'
				}
			]
		},
		{
			category: 'Location',
			subCategories: [
				{
					subCategory: 'Activate Your Voice',
					subCategoryLink: '#'
				},
				{
					subCategory: 'Oscroft, Nr Tarvin,',
					subCategoryLink: '#'
				},
				{
					subCategory: 'Chester,',
					subCategoryLink: '#'
				},
				{
					subCategory: 'CH3 8NL',
					subCategoryLink: '#'
				}
			]
		}
	],
	subFooter: {
		copywriteText: '© 2026 Activate Your Voice. All rights reserved.'
	}
}
