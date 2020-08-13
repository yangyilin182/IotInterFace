module.exports = {

    summary:function(){
        return "replace response data by local response now";
    },

    //mark if use local response
    shouldUseLocalResponse : function(req,reqBody){
        if(/checkVersionAndLogin/.test(req.url)){   //被mock接口判断选择
            req.replaceLocalFile = 0;
            return true;
        }

        if(/reply/.test(req.url)){
            req.replaceLocalFile = 1;
            return true;
        }

            return false;
    },

    dealLocalResponse : function(req,reqBody,callback){
        if(req.replaceLocalFile==0){
            request = require('request-json');
            var client = request.createClient('http://127.0.0.1');
              client.get('/checkVersionAndLogin', function(err, res, body)  //触发mock，到moco中获取mock响应数据
                {
                    console.log('the resp is ------------------------->',res.statusCode,res.headers,body);
                    var newDataStr=JSON.stringify(body);
                    callback(res.statusCode,res.headers,newDataStr); //mock数据返回给客户端
                }
            );
        }
    }
};