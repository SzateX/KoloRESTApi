(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-a31ce2fe"],{"1e93":function(t,e,i){"use strict";var n=i("5cc3"),a=i.n(n);a.a},"291b":function(t,e,i){"use strict";i.r(e);var n=function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("div",[i("articles-list",{staticStyle:{"margin-left":"5px","margin-right":"5px"},attrs:{articles:t.articles}}),i("v-pagination",{attrs:{length:t.pagination.pageCount,"prev-icon":"mdi-chevron-left","next-icon":"mdi-chevron-right"},on:{input:t.paginationClicked},model:{value:t.pagination.currentPage,callback:function(e){t.$set(t.pagination,"currentPage",e)},expression:"pagination.currentPage"}})],1)},a=[],r=(i("a481"),i("d225")),c=i("b0b4"),s=i("308d"),o=i("6bb5"),u=i("4e2b"),l=i("9ab4"),p=i("60a3"),g=i("e03f"),h=i("6124"),f=function(t){function e(){return Object(r["a"])(this,e),Object(s["a"])(this,Object(o["a"])(e).apply(this,arguments))}return Object(u["a"])(e,t),Object(c["a"])(e,[{key:"beforeCreate",value:function(){this.articlesService=new g["a"],this.pagination=new h["a"](1,3,3)}},{key:"mounted",value:function(){var t=+this.$route.params.page;(void 0===t||isNaN(t))&&(t=1),this.pagination.currentPage=t,this.paginationClicked(t)}},{key:"paginationClicked",value:function(t){var e=this;this.articlesService.getArticles(t,this.pagination.itemsPerPage,!1).then(function(t){e.articles=t.results,e.pagination.itemCount=t.count}),this.$router.replace({name:"articles",params:{page:""+t}})}},{key:"data",value:function(){return{articles:this.articles,pagination:this.pagination}}}]),e}(p["c"]);f=l["a"]([p["a"]],f);var b=f,v=b,d=(i("1e93"),i("2877")),m=Object(d["a"])(v,n,a,!1,null,null,null);e["default"]=m.exports},"5cc3":function(t,e,i){},6124:function(t,e,i){"use strict";i.d(e,"a",function(){return r});var n=i("d225"),a=i("b0b4"),r=function(){function t(e,i,a){Object(n["a"])(this,t),this.currentPage=e,this.itemCount=i,this.itemsPerPage=a}return Object(a["a"])(t,[{key:"pageCount",get:function(){return Math.ceil(this.itemCount/this.itemsPerPage)}}]),t}()}}]);
//# sourceMappingURL=chunk-a31ce2fe.990dccb7.js.map