// Social Links
// ------------
// Description: The social links data for the website.

export interface SocialLink {
	name: string
	link: string
	icon: string
}

export const socialLinks: SocialLink[] = [
	{
		name: 'facebook',
		link: 'https://www.facebook.com/activateyourvoice',
		icon: 'fb-icon'
	},
	{
		name: 'twitter',
		link: 'https://twitter.com/activateyourvoice',
		icon: 'twitter-icon'
	}
]
