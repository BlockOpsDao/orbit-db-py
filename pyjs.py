from ast import Or
from javascript import require

OrbitDB = require('orbit-db')
IPFS = require('ipfs')

ipfs = IPFS.create()
orbitdb = OrbitDB.createInstance(ipfs)

db = orbitdb.log("hello")
db.load()

# (async function () {
#   const ipfs = await IPFS.create()
#   const orbitdb = await OrbitDB.createInstance(ipfs)

#   // Create / Open a database
#   const db = await orbitdb.log("hello")
#   await db.load()

#   // Listen for updates from peers
#   db.events.on("replicated", address => {
#     console.log(db.iterator({ limit: -1 }).collect())
#   })

#   // Add an entry
#   const hash = await db.add("world")
#   console.log(hash)

#   // Query
#   const result = db.iterator({ limit: -1 }).collect()
#   console.log(JSON.stringify(result, null, 2))
# })()
