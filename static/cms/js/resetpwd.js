$(function(){
    $("#submit").click(function (event) {
        //event.preventDefault
        //组织按钮默认的提交表单事件
        event.preventDefault();

        var oldpwdE = $("input[name=oldpwd]");
        var newpwdE = $("input[name=newpwd]");
        var newpwd2E = $("input[name=newpwd2]");

        var oldpwd = oldpwdE.val();
        var newpwd = newpwdE.val();
        var newpwd2 = newpwd2E.val();

        //要在meta标签中渲染一个csrf-token
        //在ajax请求的投不中设置一个X-CSRFtoken

        zlajax.post({
            'url':'/cms/resetpwd',
            'data':{
                'oldpwd':oldpwd,
                'newpwd':newpwd,
                'newpwd2':newpwd2
            },
            'success':function(data){
                console.log(data);
            },
            'fail':function (error) {
                console.log(error);

            }
        })
    });
});