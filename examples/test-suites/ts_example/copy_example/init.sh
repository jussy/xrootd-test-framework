#!/bin/bash
set -e

function log () {
	echo `date +['%T']` $@
}

log "Initializing test case on slave" @slavename@ "..."

cd /data

if [[ @slavename@ =~ ds ]]; then
  
	if [ -f testfile ]; then
		rm testfile
	fi
	
	truncate --size=50M testfile
	chown daemon.daemon testfile

elif [[ @slavename@ =~ client ]]; then
	
	log "Mounting xrootd fuse on @slavename@ ..."
	
	export XRD_DEBUG_LEVEL=3
	export XRDDEBUG=3
	mount -t fuse xrootdfs /xrootdfs -o rdr=xroot://metamanager1.xrd.test:1094//data,uid=daemon

else
	log "Nothing to initialize." 
fi
