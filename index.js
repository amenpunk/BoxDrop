const fs = require('fs');
const prompt = require('prompt');
const dotenv = require("dotenv")
dotenv.config();
const { Dropbox } = require('dropbox'); // eslint-disable-line import/no-unresolved
let { token, link } = process.env

const route = "/lazzy/tortrix.png"

const dbx = new Dropbox({ accessToken: token});

function list(){
    dbx.filesListFolder({ path: '/lazzy' })
        .then((response) => {
            let { entries } = response.result
            entries.map(e => console.log(e))
        })
        .catch((err) => {
            console.log(err);
        });
}

function fromFiles(){
    try{
        dbx.filesDownload({ path: route})
            .then((response) => {
                let {name, fileBinary,} = response.result
                fs.writeFile(name, fileBinary, 'binary', function (err) {
                    if (err) { throw err; }
                    console.log('File: ' + name + ' saved.');
                });
            })
            .catch((err) => {
                console.log(err)
            });
    }catch(e){
        console.log(e)
    }
}

function fromLink(){
    try{
        dbx.sharingGetSharedLinkFile({ url: link})
            .then((data) => {
                let { name, fileBinary } = data.result
                fs.writeFile(name, fileBinary, 'binary', (err) => {
                    if (err) { throw err; }
                    console.log(`File: ${name} saved.`);
                });
            })
            .catch((err) => {
                console.log(err)
            });
    }catch(e){
        console.log(e)
    }
}

fromFiles()
//fromLink()

