import { Client } from '@notionhq/client'

const notion = new Client({ auth: process.env.NOTION_API_KEY })
const LOG_ID = '55325b90309e4abe8a1744fa0a4fde26'

async function run() {
  const title = new Date()
  const res = await notion.pages.create({
    parent: { database_id: LOG_ID },
    properties: {
      title,
      Date: {
        id: 'Date',
        name: 'Date',
        start: new Date()
      }
    }
  })
  console.dir(res)
}

run()

