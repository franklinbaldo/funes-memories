import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const blog = defineCollection({
	// Load Markdown and MDX files in the `src/content/blog/` directory.
	loader: glob({ base: './src/content/blog', pattern: '**/*.{md,mdx}' }),
	// Type-check frontmatter using a schema
	schema: ({ image }) =>
		z.object({
			title: z.string(),
			description: z.string(),
			// Transform string to Date object
			pubDate: z.coerce.date(),
			updatedDate: z.coerce.date().optional(),
			heroImage: image().optional(),
			tags: z.array(z.string()).optional(),
			draft: z.boolean().optional(),

            // New fields for Funes Archive
            id: z.string().optional(),
            type: z.array(z.string()).optional(),
            project: z.array(z.string()).optional(),
            entities: z.array(z.string()).optional(),
            related: z.array(z.string()).optional(),
            committed: z.string().optional(),
		}),
});

export const collections = { blog };
