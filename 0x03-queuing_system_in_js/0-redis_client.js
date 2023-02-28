import { createClient } from 'redis';

const client = createClient();

client.on('error', err => console.log('Redis client not connected to the server: ', err));

await client.connect();

await client.set('key', 'value');
const value = await client.get('key');
await client.disconnect();