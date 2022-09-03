# docker run -itd -w /Users/venky/ns-3 -v /playground/ns-3/ns-allinone-3.35/ns-3.35:/ns-3 ns3 bash -c "cd ns-3 && ./waf configure --enable-tests --enable-examples --out=build/debian"
test="/playground/ns-3/ns-allinone-3.35/ns-3.35:/ns-3 ns3 bash -c"
relDir=$(echo $PWD | cut -d/ -f1-3)
test="${relDir}${test}"
docker run -itd -w /ns-3 -v $test "cd ns-3 && ./waf configure --enable-tests --enable-examples --out=build/debian"