<template>
    <div>
        <div class="hello">This is about page</div>
        <div style="margin-top: 10px;">
            <el-button style="width: 110px;" type="primary" size="small" @click="onClick1">XMLHttpRequest</el-button>
        </div>
        <div style="margin-top: 10px;">
            <el-button style="width: 110px;" type="primary" size="small" @click="onClick2">Fetch GET</el-button>
        </div>
        <div style="margin-top: 10px;">
            <el-button style="width: 110px;" type="primary" size="small" @click="onClick3">Fetch POST</el-button>
        </div>
    </div>
    
</template>
<script>
module.exports = {
    data: function() {
        return {

        }
    },
    methods: {
        async onClick1() {
            var xhr = new XMLHttpRequest();
            xhr.open('GET', '/get_info', true);
            xhr.onload = function() {
                if(xhr.status >= 200 && xhr.status < 300) {
                    var responseData = xhr.responseText;
                    console.log(responseData);
                }else{
                    console.error('failed: ', xhr.status, xhr.statusText);
                }
            };
            xhr.onerror = function() {
                console.error('request error');
            }
            xhr.send();
            console.log("load");
        },

        async onClick2() {
            fetch('/get_info')
            .then(response => response.json())
            .then(responseData => {
                console.log('Response data:', responseData);
            })
            .catch(function(error) {
                console.error('Error：', error);
            });
        },

        async onClick3() {
            const url = '/set_info';
            const jsonData = {
                'AAA': 1,
                'BBB': 2
            };
            const options = {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(jsonData)
            };
            fetch(url, options)
            .then(response => response.json())
            .then(responseData => {
                console.log('Response data:', responseData);
            })
            .catch(error => {
                console.error('Error: ', error);
            });
        }

    }
    
}
</script>

<style>

</style>
