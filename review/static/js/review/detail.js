const likeFormTag = document.querySelector('.like-form')
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;


likeFormTag.addEventListener('submit', function (event) {
  event.preventDefault()
  axios({
    method: 'post',
    url: `/review/${likeFormTag.dataset.reviewPk}/like/`,
    headers: { 'X-CSRFToken': csrftoken },
  }).then((response) => {
    // 좋아요 아이콘 토글
    const heartIcon = document.querySelector('.heart-icon')
    heartIcon.classList.toggle('bi-heart')
    heartIcon.classList.toggle('bi-heart-fill')

    // 좋아요 갯수 변경
    const heartCnt = document.querySelector('.like-cnt')
    heartCnt.innerText = response.data.like_cnt
  })
})